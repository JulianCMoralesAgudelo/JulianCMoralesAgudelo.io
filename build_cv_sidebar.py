"""Render the reviewed CV content in a sidebar layout inspired by user references."""
import ast
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parent
sections={
 'Perfil profesional': [
  'Administrador de Bases de Datos con experiencia en gestión, parchado crítico y remediación de vulnerabilidades en Oracle (12c/19c), SQL Server, PostgreSQL y Amazon RDS.',
  'Especializado en almacenamiento, alta disponibilidad (Oracle RAC y failover en RDS), incidentes y automatización con Bash y PowerShell. Formado en Desarrollo de Software e Ingeniería de Sistemas; cursa una especialización en Ciencia de Datos.'
 ],
 'Experiencia actual': [
  '<b>Tata Consultancy Services (TCS)</b><br/><font color="#98501f"><b>Analista de Bases de Datos (DBA)</b></font><br/><font color="#425469">Enero de 2023 - Actualidad · Proyecto Bancolombia ITO</font>',
  '<b>Parchado y vulnerabilidades.</b> Ejecuté el ciclo de remediación crítica en pruebas y producción y apliqué parches a binarios y motores Oracle 12c/19c.',
  '<b>Operación.</b> Depuré inventarios y parches anteriores. Gestioné tablespaces, datafiles y ASM en Oracle RAC y Linux; atendí incidentes de Nivel 2/3 bajo SLA.',
  '<b>Automatización.</b> Automaticé el parchado remoto de SQL Server, la recolección de logs y las validaciones con Bash y PowerShell.',
  '<b>AWS.</b> Gestioné Amazon RDS para Oracle, SQL Server, PostgreSQL y MySQL; realicé pruebas de failover en simulacros de recuperación.'
 ],
 'Experiencia anterior': [
  '<b>Emergía Customer Care</b><br/><font color="#98501f">Analista de Datos Junior</font><br/>2021 - 2023',
  'Diseñé análisis de bases de datos, tipificaciones y tableros de KPI para mejorar la visibilidad operativa y los reportes.',
  'Estructuré estrategias de marcación y priorización para mejorar el contacto y la conversión. Automaticé la consolidación de datos en Excel para reportes de adherencia y productividad.',
  '<b>Soluciones IES</b><br/><font color="#98501f">Técnico de Soporte</font><br/>2015 - 2020',
  'Mantuve hardware, software y sistemas operativos. Apoyé la continuidad de bases de datos con scripts de monitoreo, respaldos y pruebas de restauración.'
 ],
 'Formación académica': [
  '<b>Especialización en Ciencia de Datos y Analítica</b><br/>En curso',
  '<b>Ingeniería de Sistemas</b><br/>UNAD · Etapa final',
  '<b>Tecnología en Desarrollo de Software</b><br/>Institución Universitaria Digital de Antioquia',
  '<b>Tecnología en Electrónica</b><br/>ITM'
 ]
}
courses=[('Bases de Datos en AWS','1426','ago. 2026'),('Amazon DynamoDB','6142','oct. 2026'),('Big Data en AWS','1511','oct. 2026'),('AWS: Cómputo con EC2','3073','ago. 2026'),('AWS: Roles y Seguridad con IAM','3044','ago. 2026'),('Infraestructura como Código en AWS','1717','ago. 2026'),('Fundamentos de Python','12286','sep. 2026')]
PDF=ROOT/'output'/'pdf'/'Julian_Camilo_Morales_Agudelo_CV.pdf'
W,H=A4
NAVY='#07111f'; ACCENT='#f58b45'; BODY='#263746'; SOFT='#d8e3ed'
c=canvas.Canvas(str(PDF),pagesize=A4)
c.setTitle('Hoja de vida | Julián Camilo Morales Agudelo');c.setAuthor('Julián Camilo Morales Agudelo')
def box(x,y,w,h,color):
 c.setFillColor(colors.HexColor(color));c.rect(x,H-y-h,w,h,stroke=0,fill=1)
def txt(s,x,y,w,size=9.5,color=BODY,bold=False,leading=None):
 p=Paragraph(s,ParagraphStyle('cv',fontName='Helvetica-Bold' if bold else 'Helvetica',fontSize=size,leading=leading or size*1.4,textColor=colors.HexColor(color)))
 _,h=p.wrap(w,H);p.drawOn(c,x,H-y-h);return y+h
def rule(x,y,w,color='#ced8e2'):
 c.setStrokeColor(colors.HexColor(color));c.setLineWidth(.6);c.line(x,H-y,x+w,H-y)
def title(s,x,y,w,side=False):
 color=ACCENT if side else NAVY
 y=txt(s.upper(),x,y,w,10.5,color,True)
 rule(x,y+6,w,ACCENT if side else '#c9d5df')
 return y+19
def side_content(s,y,size=9.1):return txt(s,23,y,164,size,'#ffffff')+10
def base(page):
 box(0,0,W,H,'#ffffff');box(0,0,210,H,NAVY)
 box(210,0,1,H,ACCENT)
 txt('Julián Camilo<br/>Morales Agudelo',23,773,164,12,ACCENT,True)
 txt('HOJA DE VIDA',236,801,240,7.3,NAVY,True)
 txt(f'{page:02} / 02',W-67,801,45,7.3,NAVY,True)
 rule(236,791,W-263)
def circle_photo():
 cx,cy,r=105,H-103,66
 c.setFillColor(colors.HexColor(ACCENT));c.circle(cx,cy,r+3,stroke=0,fill=1)
 c.saveState();p=c.beginPath();p.circle(cx,cy,r);c.clipPath(p,stroke=0)
 c.drawImage(ImageReader(str(ROOT/'assets'/'portrait.jpg')),cx-r,cy-r,2*r,2*r,preserveAspectRatio=True,anchor='c',mask='auto');c.restoreState()
X=236; MW=W-X-27
base(1);circle_photo()
y=title('Contacto',23,191,164,True)
y=side_content('Medellín, Colombia',y)
y=side_content('<link href="mailto:juliancmorales10@gmail.com" color="#ffffff">juliancmorales10<br/>@gmail.com</link>',y)
y=side_content('<link href="https://www.linkedin.com/in/juliancmorales/" color="#ffffff">LinkedIn<br/>/in/juliancmorales/</link>',y)
y=side_content('<link href="https://github.com/JulianCMoralesAgudelo" color="#ffffff">GitHub<br/>JulianCMoralesAgudelo</link>',y)
y=title('Tecnologías',23,y+14,164,True)
for s in ['<b>Bases de datos</b><br/>Oracle 12c/19c · SQL Server<br/>PostgreSQL · MySQL', '<b>Operación Oracle</b><br/>RAC · RMAN · ASM<br/>Tablespaces · Datafiles', '<b>Nube y sistemas</b><br/>Amazon RDS · EC2 · IAM<br/>Linux · Docker', '<b>Automatización</b><br/>Bash · PowerShell<br/>Python · Terraform · Git']:
 y=side_content(s,y)
y=title('Trabajo',23,y+12,164,True)
y=side_content('Incidentes SLA / ITSM<br/>Colaboración con fabricantes<br/>Aprendizaje autónomo',y,8.8)
assert y<770,('sidebar1',y)
box(X,35,34,4,ACCENT)
y=txt('JULIÁN CAMILO<br/>MORALES AGUDELO',X,54,MW,24,NAVY,True,28)
y=txt('ADMINISTRADOR DE BASES DE DATOS',X,y+12,MW,10.4,'#98501f',True)
y=title('Perfil profesional',X,y+24,MW)
for s in sections['Perfil profesional']:y=txt(s,X,y,MW,9.5)+9
y=title('Experiencia profesional',X,y+13,MW)
for i,s in enumerate(sections['Experiencia actual']):
 y=txt(s,X,y,MW,9.5)+ (15 if i==0 else 10)
assert y<778,('main1',y)
c.showPage()
base(2)
y=title('Formación continua',23,36,164,True)
for name,cid,date in courses:
 s=f'<link href="https://platzi.com/p/juliancamilomoralesagudelo/curso/{cid}-course/diploma/detalle/" color="#ffffff"><b>{name}</b></link><br/><font color="{SOFT}">Platzi · {date}</font>'
 y=side_content(s,y,9.1)+7
y=title('Otros cursos',23,y+8,164,True)
y=side_content('Database Programming with SQL (2024)<br/><br/>Database Design (2023)<br/><br/>Administración Oracle 21c<br/><br/>Linux y Shell Script<br/><br/>PostgreSQL y Docker',y,8.9)
assert y<770,('sidebar2',y)
txt('JULIÁN CAMILO MORALES AGUDELO',X,37,MW,12,NAVY,True)
txt('Trayectoria y formación',X,59,MW,9.5)
y=title('Experiencia anterior',X,100,MW)
for i,s in enumerate(sections['Experiencia anterior']):y=txt(s,X,y,MW,9.5)+13
y=title('Formación académica',X,y+15,MW)
for s in sections['Formación académica']:y=txt(s,X,y,MW,9.5)+14
y=title('Formación complementaria',X,y+13,MW)
y=txt('SQL y diseño de bases de datos (Oracle Academy); administración Oracle 21c, Linux y Shell Scripting, PostgreSQL y Docker.',X,y,MW,9.5)
assert y<778,('main2',y)
c.save()
r=PdfReader(str(PDF));assert len(r.pages)==2
alltext=' '.join(p.extract_text() for p in r.pages)
assert 'orquestador' not in alltext.lower()
assert 'Enero de 2023' in alltext
print(PDF)

