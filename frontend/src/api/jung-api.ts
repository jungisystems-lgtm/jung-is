const REQUEST_TIMEOUT_MS = 8_000;

/**
 * Server-side HTTP boundary for jung-api. Add typed operations here as contracts
 * become available; do not put booking, lead, or messaging rules in this app.
 */
export async function getFromJungApi<T>(path: `/${string}`): Promise<T> {
  const baseUrl = process.env.JUNG_API_URL;

  if (!baseUrl) {
    throw new Error('JUNG_API_URL is required to call jung-api');
  }

  const url = new URL(path, baseUrl.endsWith('/') ? baseUrl : `${baseUrl}/`);
  const response = await fetch(url, {
    headers: { Accept: 'application/json' },
    signal: AbortSignal.timeout(REQUEST_TIMEOUT_MS),
    cache: 'no-store',
  });

  if (!response.ok) {
    console.error('jung-api request failed', {
      path,
      status: response.status,
      statusText: response.statusText,
    });
    throw new Error(
      `jung-api request failed: ${response.status} ${response.statusText}`,
    );
  }

  return (await response.json()) as T;
}
