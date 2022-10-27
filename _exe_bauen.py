import os

# exe erzeugen

# os.system("pyinstaller --onefile --noconsole PlotterWizard.py")

os.system("venv\\Scripts\\pyinstaller --onefile --noconsole --icon=icon.ico main.py --name BeBack4ever")
#os.system("venv\\Scripts\\pyinstaller --onefile --icon=icons\\laser_YXc_icon.ico PlotterWizard.py")

# installer erstellen
#os.system("iscc dist\\PlotterWizard.iss")