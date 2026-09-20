import { siteConfig } from '@/config/site';

export default function HomePage() {
  return (
    <>
      <section className="hero">
        <div className="container hero-inner">
          <p className="eyebrow">Jung · Tecnología con propósito</p>
          <h1>Conversaciones que se convierten en mejores experiencias.</h1>
          <p className="hero-copy">
            Creamos herramientas digitales para que los negocios atiendan mejor,
            aprendan de cada interacción y crezcan con claridad.
          </p>
          <a className="button" href={siteConfig.primaryAction.href}>
            {siteConfig.primaryAction.label}
          </a>
        </div>
      </section>
      <section className="section" id="que-hacemos">
        <div className="container section-grid">
          <p className="eyebrow">Qué hacemos</p>
          <div>
            <h2>Una base sólida para relaciones que duran.</h2>
            <p>
              Unimos sitios claros con capacidades que ayudan a captar
              oportunidades, responder con contexto y hacer seguimiento.
            </p>
          </div>
        </div>
      </section>
      <section className="section section-tinted" id="como-trabajamos">
        <div className="container section-grid">
          <p className="eyebrow">Cómo trabajamos</p>
          <div>
            <h2>Empezamos por lo que genera valor ahora.</h2>
            <p>
              Construimos de forma progresiva: una experiencia útil hoy,
              preparada para mejorar con lo que aprendamos de clientes reales.
            </p>
          </div>
        </div>
      </section>
    </>
  );
}
