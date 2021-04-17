#Don'r forget to take a look at this! : https://developers.google.com/slides/quickstart/python
import MyStatisticsLib


DenuncieSicilia = [3.6, 3.0, 23.2, 3.2, 13.0, 13.3, 25.2, 5.2, 10.3]
DenuncieLazio = [6.3, 4.3, 4.6, 80.7, 4.1]
DenuncieVeneto = [6.8, 16.3, 2.4, 19.2, 14.3, 27.2, 13.8]

MyStatisticsLib.SetTrutleSpeed(0)
ProvincieSicilia = MyStatisticsLib.Aereogram(
    "Provincie della Sicilia", 
    DenuncieSicilia, 
    ["#ff3333", "#ff0000", "#ff3333", "#ff6666", "#ffbbbb", "#ffcccc", "#ff9999", "#ffaaaa", "#ff9999"], 
    ["Agrigento", "Caltanissetta", "Catania", "Trapani", "Enna", "Messina", "Palermo", "Ragusa", "Siracusa"], 
    230, 
    False, 
    WantsToWriteStatisticalValues=True,
    DoesHeWantOuterBorder= True
)

ProvincieLazio = MyStatisticsLib.Aereogram(
    "Provincie del Lazio", 
    DenuncieLazio, 
    ["#ddffdd", "#44ff44", "#99ff99", "#00ff00", "#77ff77"], 
    ["Frosinone", "Latina", "Rieti", "Roma", "Vitebro"], 
    230, 
    False, 
    WantsToWriteStatisticalValues= True,
    DoesHeWantOuterBorder= True
)

ProvincieVeneto = MyStatisticsLib.Aereogram(
    "Provincie del Veneto", 
    DenuncieVeneto, 
    ["#0000ff", "#6666ff", "#3333ff", "#6666ff", "#7777ff", "#5555ff", "#9999ff"], 
    ["Balluno", "Padova", "Rovigo", "Treviso", "Venezia", "Verona", "Vicenza"], 
    230, 
    False, 
    WantsToWriteStatisticalValues= True,
    DoesHeWantOuterBorder= True
)

Values = [10, 12, 15, 14, 16, 17, 9, 7]

ProvincieSicilia.LogStatistics()
ProvincieSicilia.draw()

MyStatisticsLib.AwaitInputForNextGraph()
MyStatisticsLib.clearscreen()

ProvincieLazio.LogStatistics()
ProvincieLazio.draw()

MyStatisticsLib.AwaitInputForNextGraph()
MyStatisticsLib.clearscreen()

ProvincieVeneto.LogStatistics()
ProvincieVeneto.draw()




MyStatisticsLib.FinishedPrinting()