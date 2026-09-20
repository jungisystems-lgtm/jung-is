import Link from 'next/link';
import { siteConfig } from '@/config/site';

export function SiteHeader() {
  return (
    <header className="site-header">
      <div className="container header-inner">
        <Link
          className="brand"
          href="/"
          aria-label={`${siteConfig.name}, inicio`}
        >
          {siteConfig.name}
        </Link>
        <nav aria-label="Navegación principal">
          {siteConfig.navigation.map((item) => (
            <Link href={item.href} key={item.href}>
              {item.label}
            </Link>
          ))}
        </nav>
        <a className="header-contact" href={siteConfig.primaryAction.href}>
          {siteConfig.primaryAction.label}
        </a>
      </div>
    </header>
  );
}
