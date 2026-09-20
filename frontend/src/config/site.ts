// Site-specific copy and branding live here until jung-api provides this configuration.
export const siteConfig = {
  name: 'Jung',
  description:
    'Soluciones digitales que convierten conversaciones en oportunidades.',
  navigation: [
    { label: 'Qué hacemos', href: '#que-hacemos' },
    { label: 'Cómo trabajamos', href: '#como-trabajamos' },
  ],
  primaryAction: {
    label: 'Conoce Jung',
    href: '#que-hacemos',
  },
} as const;
