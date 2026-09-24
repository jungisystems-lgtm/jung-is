"""Seed unpublished Jung landing drafts in Spanish and English.

The reference design included unverified testimonials and performance figures.
Those groups are deliberately absent. Publication requires human review.
"""

from django.db import migrations

SPANISH_COPY = {
    "seo": {
        "title": "Jung | Convierte conversaciones en citas",
        "description": "Tu página web, WhatsApp, IA y calendario trabajando juntos para que "
        "ninguna oportunidad se pierda.",
    },
    "shared_text": {
        "navigation_labels": {
            "solutions": "Soluciones",
            "how_it_works": "Cómo funciona",
            "use_cases": "Casos de uso",
            "pricing": "Precios",
            "faq": "FAQ",
            "contact": "Contacto",
        },
        "action_labels": {"book_demo": "Agendar demo", "watch_demo": "Ver Jung en acción"},
        "footer_tagline": "Más allá de lo posible.",
    },
    "hero": {
        "eyebrow": "Sistemas inteligentes para un mundo en evolución",
        "heading_lead": "Convierte conversaciones",
        "heading_accent": "en citas.",
        "description": "Tu página web, WhatsApp, IA y calendario trabajando juntos para que "
        "ninguna oportunidad se pierda y tu negocio siga creciendo.",
        "side_note": "Inteligencia que expande horizontes",
        "highlights": [
            {"id": "opportunities", "label": "Más oportunidades de venta"},
            {"id": "time", "label": "Menos tiempo en tareas manuales"},
            {"id": "always_on", "label": "Un proceso comercial siempre activo"},
        ],
    },
    "problem": {
        "eyebrow": "El problema",
        "heading": "Tienes contactos, pero se pierden.",
        "description": "Generas interés en tu página, redes o WhatsApp, pero la mayoría de "
        "esos contactos no se convierten en oportunidades reales.",
        "items": [
            {"id": "late_replies", "label": "Respuestas tardías"},
            {"id": "lost_conversations", "label": "Conversaciones que se pierden"},
            {"id": "manual_followup", "label": "Seguimiento manual"},
            {"id": "disconnected_tools", "label": "Herramientas desconectadas"},
            {"id": "unanswered_prospects", "label": "Prospectos que dejan de responder"},
        ],
    },
    "solution": {
        "eyebrow": "La solución",
        "heading": "Un sistema completo para tu crecimiento.",
        "description": "Jung conecta tu página web, WhatsApp, inteligencia artificial y "
        "calendario en un solo flujo comercial, para que puedas atraer, "
        "conversar, dar seguimiento y agendar más citas, sin fricción.",
        "items": [
            {
                "id": "attract",
                "heading": "Atrae",
                "description": "El prospecto llega desde tu página, campaña o canal.",
            },
            {
                "id": "converse",
                "heading": "Conversa",
                "description": "La IA responde, califica y mantiene la conversación.",
            },
            {
                "id": "follow_up",
                "heading": "Da seguimiento",
                "description": "El sistema realiza recordatorios y mensajes automáticos.",
            },
            {
                "id": "book",
                "heading": "Agenda",
                "description": "El prospecto elige un horario en tu calendario.",
            },
            {
                "id": "sell",
                "heading": "Vende más",
                "description": "Convierte más oportunidades en clientes.",
            },
        ],
    },
    "audiences": {
        "eyebrow": "Ideal para",
        "heading": "Funciona para diferentes tipos de negocios.",
        "description": "Cualquier empresa que reciba consultas, cotizaciones o agende citas "
        "puede beneficiarse de Jung.",
        "items": [
            {
                "id": "retail",
                "heading": "Comercio minorista",
                "description": "Tiendas, boutiques, servicios locales.",
            },
            {
                "id": "wellness",
                "heading": "Salud y bienestar",
                "description": "Clínicas, consultorios, centros de estética.",
            },
            {
                "id": "education",
                "heading": "Educación",
                "description": "Academias, cursos, formación profesional.",
            },
            {
                "id": "b2b",
                "heading": "Servicios B2B",
                "description": "Consultoras, agencias, proveedores.",
            },
            {
                "id": "hospitality",
                "heading": "Hospitalidad",
                "description": "Restaurantes, hoteles, eventos.",
            },
        ],
    },
    "closing_cta": {
        "left_note": "Un futuro más conectado comienza hoy.",
        "heading": "¿Listo para convertir más oportunidades en clientes?",
        "description": "Agenda una demostración y descubre cómo Jung puede impulsar tu negocio.",
        "right_note": "Ideas, personas, sistemas: un mañana más amplio.",
    },
}

ENGLISH_COPY = {
    "seo": {
        "title": "Jung | Turn conversations into appointments",
        "description": "Your website, WhatsApp, AI, and calendar working together so "
        "opportunities do not slip away.",
    },
    "shared_text": {
        "navigation_labels": {
            "solutions": "Solutions",
            "how_it_works": "How it works",
            "use_cases": "Use cases",
            "pricing": "Pricing",
            "faq": "FAQ",
            "contact": "Contact",
        },
        "action_labels": {"book_demo": "Book a demo", "watch_demo": "See Jung in action"},
        "footer_tagline": "Beyond what is possible.",
    },
    "hero": {
        "eyebrow": "Intelligent systems for an evolving world",
        "heading_lead": "Turn conversations",
        "heading_accent": "into appointments.",
        "description": "Your website, WhatsApp, AI, and calendar working together so no "
        "opportunity slips away and your business keeps growing.",
        "side_note": "Intelligence that expands horizons",
        "highlights": [
            {"id": "opportunities", "label": "More sales opportunities"},
            {"id": "time", "label": "Less time on manual tasks"},
            {"id": "always_on", "label": "An always-on sales process"},
        ],
    },
    "problem": {
        "eyebrow": "The problem",
        "heading": "You have leads, but they slip away.",
        "description": "You generate interest through your website, social channels, or "
        "WhatsApp, but many of those contacts never become real opportunities.",
        "items": [
            {"id": "late_replies", "label": "Slow replies"},
            {"id": "lost_conversations", "label": "Lost conversations"},
            {"id": "manual_followup", "label": "Manual follow-up"},
            {"id": "disconnected_tools", "label": "Disconnected tools"},
            {"id": "unanswered_prospects", "label": "Prospects who stop replying"},
        ],
    },
    "solution": {
        "eyebrow": "The solution",
        "heading": "A complete system for your growth.",
        "description": "Jung connects your website, WhatsApp, AI, and calendar in one sales "
        "flow so you can attract, engage, follow up, and book more "
        "appointments with less friction.",
        "items": [
            {
                "id": "attract",
                "heading": "Attract",
                "description": "A prospect arrives from your website, campaign, or "
                "another channel.",
            },
            {
                "id": "converse",
                "heading": "Engage",
                "description": "AI responds, qualifies, and keeps the conversation going.",
            },
            {
                "id": "follow_up",
                "heading": "Follow up",
                "description": "The system sends reminders and automated messages.",
            },
            {
                "id": "book",
                "heading": "Book",
                "description": "The prospect chooses a time in your calendar.",
            },
            {
                "id": "sell",
                "heading": "Grow sales",
                "description": "Turn more opportunities into customers.",
            },
        ],
    },
    "audiences": {
        "eyebrow": "Who it is for",
        "heading": "Built for different kinds of businesses.",
        "description": "Any business that receives inquiries, sends quotes, or books "
        "appointments can benefit from Jung.",
        "items": [
            {
                "id": "retail",
                "heading": "Retail",
                "description": "Shops, boutiques, and local services.",
            },
            {
                "id": "wellness",
                "heading": "Health and wellness",
                "description": "Clinics, practices, and beauty centers.",
            },
            {
                "id": "education",
                "heading": "Education",
                "description": "Academies, courses, and professional training.",
            },
            {
                "id": "b2b",
                "heading": "B2B services",
                "description": "Consultancies, agencies, and suppliers.",
            },
            {
                "id": "hospitality",
                "heading": "Hospitality",
                "description": "Restaurants, hotels, and events.",
            },
        ],
    },
    "closing_cta": {
        "left_note": "A more connected future starts today.",
        "heading": "Ready to turn more opportunities into customers?",
        "description": "Book a demo and see how Jung can help your business grow.",
        "right_note": "Ideas, people, systems: a wider tomorrow.",
    },
}


def seed_landing_copy(apps, schema_editor):
    Site = apps.get_model("landing_copy", "Site")
    LandingPage = apps.get_model("landing_copy", "LandingPage")
    Revision = apps.get_model("landing_copy", "LandingCopyRevision")
    database = schema_editor.connection.alias

    site, _ = Site.objects.using(database).get_or_create(
        key="jung", defaults={"name": "Jung Intelligence Systems"}
    )
    for locale, copy in (("es-CO", SPANISH_COPY), ("en-US", ENGLISH_COPY)):
        page, _ = LandingPage.objects.using(database).get_or_create(
            site=site, slug="home", locale=locale
        )
        Revision.objects.using(database).get_or_create(
            page=page,
            version=1,
            defaults={
                "schema_version": 1,
                "copy": copy,
                "change_summary": "Initial landing draft from the reference design.",
            },
        )


class Migration(migrations.Migration):
    dependencies = [("landing_copy", "0001_initial")]

    operations = [migrations.RunPython(seed_landing_copy, migrations.RunPython.noop)]
