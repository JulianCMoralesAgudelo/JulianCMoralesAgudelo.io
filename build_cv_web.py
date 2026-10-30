"""Generate a two-page printable CV using the website's content and visual identity."""
from pathlib import Path
from html import escape
from lxml import html as lhtml
from weasyprint import HTML

root = Path(__file__).resolve().parent
source = lhtml.parse(str(root / 'index.html'))
def text(xpath):
    return ' '.join(source.xpath(xpath)[0].itertext()).strip()
def markup(xpath):
    return lhtml.tostring(source.xpath(xpath)[0], encoding='unicode', method='html')

profile = ('Administrador de Bases de Datos con experiencia en Oracle 12c/19c, SQL Server, PostgreSQL y Amazon RDS. '
           'Especializado en parchado crítico, alta disponibilidad, almacenamiento y automatización con Bash y PowerShell.')
tcs = '''<article class="tcs">
  <div class="tcs-heading"><div><p class="company"><a href="https://www.tcs.com/">Tata Consultancy Services (TCS)</a></p><h3>Analista de Bases de Datos (DBA)</h3></div><p>Ene. 2023 – Actualidad<br>Proyecto Bancolombia ITO</p></div>
  <ul>
    <li><strong>Parchado y seguridad:</strong> ejecuté la remediación de vulnerabilidades críticas en pruebas y producción y apliqué parches a Oracle 12c/19c.</li>
    <li><strong>Operación y disponibilidad:</strong> depuré inventarios y parches anteriores; gestioné tablespaces, datafiles y ASM en Oracle RAC y Linux y atendí incidentes de Nivel 2/3 bajo SLA.</li>
    <li><strong>Automatización:</strong> automaticé el parchado remoto de SQL Server, la recolección de logs y las validaciones con Bash y PowerShell.</li>
    <li><strong>Nube y recuperación:</strong> gestioné Amazon RDS para Oracle, SQL Server, PostgreSQL y MySQL y realicé pruebas de failover en simulacros de recuperación.</li>
  </ul>
</article>'''
prior = markup("//div[@class='career-grid']")
skills = '''<div class="skills-grid">
  <article><h3>Motores y almacenamiento</h3><p>Oracle 12c/19c, SQL Server, PostgreSQL, MySQL, SQL, tablespaces, datafiles y ASM.</p></article>
  <article><h3>Disponibilidad y recuperación</h3><p>Oracle RAC, RMAN, failover en Amazon RDS, parchado y respuesta a incidentes Nivel 2/3.</p></article>
  <article><h3>Automatización y nube</h3><p>Bash, PowerShell, Python, Linux, AWS EC2 e IAM, Docker, Terraform y Git/GitHub.</p></article>
</div>'''
education = markup("//div[@class='education-list']")
certifications = markup("//div[@class='certifications']")

html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><link rel="stylesheet" href="cv-web-print.css"></head><body>
<section class="page first">
  <header class="masthead">
    <div><p class="kicker">Administrador de Bases de Datos · Medellín, Colombia</p><h1>Julián Camilo Morales Agudelo</h1></div>
    <img src="assets/portrait.jpg" alt="Retrato de Julián Camilo Morales Agudelo">
  </header>
  <div class="contact-strip"><a href="mailto:juliancmorales10@gmail.com">juliancmorales10@gmail.com</a><a href="https://www.linkedin.com/in/juliancmorales/" target="_blank">linkedin.com/in/juliancmorales</a><a href="https://github.com/JulianCMoralesAgudelo" target="_blank">github.com/JulianCMoralesAgudelo</a></div>
  <main>
    <section class="profile"><h2>Perfil profesional</h2><p>{escape(profile)}</p></section>
    <div class="tech-strip"><span>Oracle 12c/19c</span><span>SQL Server</span><span>PostgreSQL</span><span>Amazon RDS</span><span>Bash y PowerShell</span></div>
    <section class="experience"><h2>Experiencia profesional</h2>{tcs}</section>
  </main>
  <footer>Julián Camilo Morales Agudelo <span>01 / 02</span></footer>
</section>
<section class="page second">
  <div class="topline"><span>Habilidades y formación</span><span>Julián Camilo Morales Agudelo</span></div>
  <main>
    <section class="prior"><h2>Experiencia anterior</h2>{prior}</section>
    <section class="skills"><h2>Habilidades clave</h2>{skills}</section>
    <section class="education"><h2>Educación y certificaciones</h2>{education}{certifications}</section>
  </main>
  <footer>Julián Camilo Morales Agudelo <span>02 / 02</span></footer>
</section></body></html>'''
out = root / 'output/pdf/Julian_Camilo_Morales_Agudelo_CV_Web.pdf'
HTML(string=html, base_url=str(root)).write_pdf(out)
print(out)
