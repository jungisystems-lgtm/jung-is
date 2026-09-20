import { siteConfig } from '@/config/site';

export function SiteFooter() {
  return (
    <footer className="site-footer">
      <div className="container footer-inner">
        <span>{siteConfig.name}</span>
        <span>Construimos para aprender, entregar y crecer.</span>
      </div>
    </footer>
  );
}
