import folium
import pandas

data= pandas.read_csv("pop.csv")

x= list(data["Lat"])
y= list(data["Long"])
r= list(data["Rank"])

def Colours(rank):
    if rank <10:
        return "green"
    elif rank< 30:
        return "orange"
    else:                                     #for defining colours
        return "red"

map= folium.Map(location=[26.84,75.56], zoom_start=6,tiles="Stamen Watercolor", height='100%', width='100%' )

fg=folium.FeatureGroup(name="My Map")       #Creating a Feature group

#Using For Loop to add multiple coordinates

for a,b,c in zip(x,y,r):

    fg.add_child(folium.CircleMarker(location=[a,b],popup=str(c),
    fill_color=Colours(c), color='grey', fill_opacity=0.7))

    

    

map.add_child(fg)

map.save("Map.html")

