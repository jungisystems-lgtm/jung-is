import { afterEach, describe, expect, it, vi } from 'vitest';
import { getFromJungApi } from '../src/api/jung-api';

afterEach(() => {
  vi.unstubAllGlobals();
  delete process.env.JUNG_API_URL;
});

describe('jung-api boundary', () => {
  it('fails clearly when its base URL is missing', async () => {
    await expect(getFromJungApi('/health')).rejects.toThrow(
      'JUNG_API_URL is required',
    );
  });

  it('uses the configured base URL and returns JSON', async () => {
    process.env.JUNG_API_URL = 'http://localhost:8000';
    const fetchMock = vi.fn().mockResolvedValue({
      ok: true,
      json: async () => ({ status: 'ok' }),
    });
    vi.stubGlobal('fetch', fetchMock);

    await expect(
      getFromJungApi<{ status: string }>('/health'),
    ).resolves.toEqual({
      status: 'ok',
    });
    expect(fetchMock).toHaveBeenCalledWith(
      new URL('http://localhost:8000/health'),
      expect.objectContaining({ cache: 'no-store' }),
    );
  });
});
