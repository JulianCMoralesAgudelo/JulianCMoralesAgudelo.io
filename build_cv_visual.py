from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'output'/'pdf'
OUT.mkdir(parents=True,exist_ok=True)
PDF=OUT/'Julian_Camilo_Morales_Agudelo_CV.pdf'
W,H=A4
INK='#07111f'; GREEN='#f58b45'; MUTED='#425469'; PAPER='#ffffff'
c=canvas.Canvas(str(PDF),pagesize=A4)
c.setTitle('Julián Camilo Morales Agudelo | Hoja de vida')
c.setAuthor('Julián Camilo Morales Agudelo')
def rect(x,top,w,h,color,r=0):
 c.setFillColor(colors.HexColor(color))
 if r:c.roundRect(x,H-top-h,w,h,r,stroke=0,fill=1)
 else:c.rect(x,H-top-h,w,h,stroke=0,fill=1)
def text(s,x,top,w,size=9.2,color=INK,bold=False,leading=None):
 st=ParagraphStyle('cv',fontName='Helvetica-Bold' if bold else 'Helvetica',fontSize=size,leading=leading or size*1.38,textColor=colors.HexColor(color))
 p=Paragraph(s,st);_,h=p.wrap(w,H);p.drawOn(c,x,H-top-h);return h
def card(title,items,x,top,w,fill='#f1f7fc',size=9.2):
 measurements=[];height=47
 for item in items:
  st=ParagraphStyle('measure',fontName='Helvetica',fontSize=size,leading=size*1.38)
  h=Paragraph(item,st).wrap(w-32,H)[1];measurements.append(h);height+=h+8
 height+=5
 rect(x,top,w,height,fill,10);rect(x,top+17,4,18,GREEN)
 text(title.upper(),x+16,top+16,w-32,11,bold=True)
 y=top+46
 for item,h in zip(items,measurements):text(item,x+16,y,w-32,size);y+=h+8
 return top+height
def footer(page):
 rect(0, H-31,W,31,INK)
 text('JULIÁN CAMILO MORALES AGUDELO',27,H-21,400,7.2,'#ffffff',True)
 text(f'HOJA DE VIDA / {page:02}',W-125,H-21,110,7.2,GREEN,True)
def background():rect(0,0,W,H,PAPER)

background();rect(0,0,W,188,INK);rect(27,27,39,4,GREEN)
text('JULIÁN CAMILO<br/>MORALES AGUDELO',27,45,385,25,'#ffffff',True,29)
text('ANALISTA DE BASES DE DATOS',28,112,380,11,GREEN,True)
text('Oracle · SQL Server · Amazon RDS',28,134,370,10,'#d8e1ec')
text('Medellín, Colombia · <link href="mailto:juliancmorales10@gmail.com" color="#ffffff">juliancmorales10@gmail.com</link>',28,157,385,8,'#ffffff')
# The existing website portrait is placed without changing its content.
photo=ROOT/'assets'/'portrait.jpg'
rect(436,32,132,132,GREEN,14)
c.saveState();clip=c.beginPath();clip.roundRect(440,H-160,124,124,11);c.clipPath(clip,stroke=0)
c.drawImage(ImageReader(str(photo)),440,H-160,width=124,height=124,mask='auto',preserveAspectRatio=True,anchor='c');c.restoreState()
left=27;gap=14;full=W-54
y=card('Perfil profesional',[
'Analista de bases de datos con experiencia en operación de Oracle y SQL Server, parchado y remediación de vulnerabilidades. Trabajo con permisos, respaldos, almacenamiento, diagnóstico de incidentes y automatización con Bash y PowerShell, además de operaciones en Amazon RDS.',
'Tecnólogo en Electrónica y en Desarrollo de Software. Finalizando Ingeniería de Sistemas en la UNAD y cursando la Especialización en Ciencia de Datos y Analítica.'
],left,204,full)
y+=14
y=card('Experiencia actual',[
'<b>Tata Consultancy Services (TCS)</b><br/><font color="#97552e"><b>Analista de Bases de Datos</b></font><br/><font color="#425469">Enero de 2023 - Actualidad · Proyecto Bancolombia ITO</font>',
'<b>Parchado y vulnerabilidades.</b> Gestiono el ciclo desde ambientes previos hasta producción: prerrequisitos, descarga y validación de parches, respaldos previos, ejecución y comprobaciones posteriores.',
'<b>Oracle.</b> Valido parches en binarios y en el motor mediante OPatch y datapatch. Respaldo binarios e inventario y depuro parches anteriores con herramientas de Oracle.',
'<b>Operación.</b> Gestiono permisos, scripts, respaldos, tablespaces, datafiles y discos ASM. Realizo monitoreo, diagnóstico y atención de incidentes en Linux, incluidos entornos Oracle RAC, y seguimiento de casos con fabricantes.',
'<b>Automatización.</b> Desarrollo y adapto scripts Bash y PowerShell para parchado remoto de SQL Server, descarga de parches, monitoreo de logs, depuración y validaciones de salud.',
'<b>AWS.</b> Opero Amazon RDS para Oracle, SQL Server, PostgreSQL y MySQL: grupos de parámetros, etiquetas, capacidad y clase de instancia. Ejecuto failover y valido la operación desde la instancia activa en pruebas de recuperación ante desastres.'
],left,y,full,size=9.3)
assert y<790,('page1 overflow',y)
text('<link href="https://www.linkedin.com/in/juliancmorales/" color="#425469">linkedin.com/in/juliancmorales/</link> · <link href="https://github.com/JulianCMoralesAgudelo" color="#425469">github.com/JulianCMoralesAgudelo</link>',left,y+12,full,8,MUTED)
footer(1);c.showPage()

background();rect(0,0,W,75,INK);rect(27,23,4,29,GREEN)
text('TRAYECTORIA Y FORMACIÓN',42,22,full-30,17,'#ffffff',True)
text('Julián Camilo Morales Agudelo',42,47,full-30,9,'#d8e1ec')
col=(full-gap)/2
yl=card('Experiencia anterior',[
'<b>Emergía Customer Care</b><br/><b>Técnico de Conducción · Analista de Datos Junior</b><br/><font color="#425469">2021 - 2023</font>',
'Análisis de bases de datos, tipificaciones y KPI. Estrategias de marcación y gestión de registros. Extracción y preparación de datos y reportes de adherencia, utilización, ventas y tiempos productivos en Excel.',
'<b>Soluciones IES</b><br/><b>Técnico de Soporte</b><br/><font color="#425469">2015 - 2020</font>',
'Instalación y administración de sistemas operativos, hardware y software. Soporte presencial y remoto, apoyo al mantenimiento de bases de datos y scripts de monitoreo y respaldos.'
],left,91,col,size=9)
yl=card('Formación académica',[
'<b>Especialización en Ciencia de Datos y Analítica</b><br/>En curso',
'<b>Ingeniería de Sistemas</b><br/>UNAD · 2023 - Actualidad<br/>En etapa final',
'<b>Tecnología en Desarrollo de Software</b><br/>Institución Universitaria Digital de Antioquia · 2019 - 2022',
'<b>Tecnología en Electrónica</b><br/>Instituto Tecnológico Metropolitano (ITM) · 2006 - 2011'
],left,yl+14,col,fill='#fff0e5',size=9)
xr=left+col+gap
yr=card('Competencias técnicas',[
'<b>Bases de datos:</b> Oracle 12c y 19c, SQL Server, RMAN, OPatch, datapatch, tablespaces y ASM. Operación en RAC y tareas operativas en PostgreSQL.',
'<b>Nube:</b> Amazon RDS, configuración, capacidad y failover.',
'<b>Automatización:</b> Bash y PowerShell. Uso diario de Linux y diagnóstico de servicios.',
'<b>Conocimientos básicos:</b> MongoDB y Redis. Terraform: formación teórica. Instalación Oracle 11g a 19c en laboratorios personales.',
'<b>Idiomas:</b> español e inglés A2 autoevaluado.'
],xr,91,col,size=9)
courses=[('Bases de Datos en AWS','1426','ago. 2026'),('Amazon DynamoDB','6142','oct. 2026'),('Big Data en AWS','1511','oct. 2026'),('AWS: Cómputo con EC2','3073','ago. 2026'),('AWS: Roles y Seguridad con IAM','3044','ago. 2026'),('Infraestructura Como Código en AWS','1717','ago. 2026'),('Fundamentos de Python','12286','sep. 2026')]
items=[f'<link href="https://platzi.com/p/juliancamilomoralesagudelo/curso/{cid}-course/diploma/detalle/" color="#234967"><b>{title}</b></link><br/>Platzi · {date}' for title,cid,date in courses]
items+=['<b>Otros cursos:</b> Database Programming with SQL (2024), Database Design (2023), administración Oracle 21c, Linux, Shell Script, PostgreSQL y Docker.']
yr=card('Cursos seleccionados',items,xr,yr+14,col,fill='#edf5ff',size=8.7)
assert max(yl,yr)<800,('page2 overflow',yl,yr)
footer(2);c.save()
r=PdfReader(str(PDF));assert len(r.pages)==2
alltext=' '.join(p.extract_text() for p in r.pages)
assert 'orquestador' not in alltext.lower()
assert 'Enero de 2023' in alltext
print(PDF);print('2 páginas; bloques:',round(y),round(yl),round(yr))
