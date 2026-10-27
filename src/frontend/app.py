import streamlit as st
import requests

st.title("🌐 Predykcja ceny najmu")

st.write("Wprowadź dane wejściowe:")

city = st.text_input("city")
type_ = st.text_input("type")
squareMeters = st.number_input("squareMeters")
rooms = st.number_input("rooms")
floor = st.number_input("floor")
floorCount = st.number_input("floorCount")
buildYear = st.number_input("buildYear", value=2000.0)
latitude = st.number_input("latitude")
longitude = st.number_input("longitude")
centreDistance = st.number_input("centreDistance")
poiCount = st.number_input("poiCount")
schoolDistance = st.number_input("schoolDistance")
clinicDistance = st.number_input("clinicDistance")
postOfficeDistance = st.number_input("postOfficeDistance")
kindergartenDistance = st.number_input("kindergartenDistance")
restaurantDistance = st.number_input("restaurantDistance")
collegeDistance = st.number_input("collegeDistance")
pharmacyDistance = st.number_input("pharmacyDistance")
ownership = st.text_input("ownership")
buildingMaterial = st.text_input("buildingMaterial")
condition = st.text_input("condition")
hasParkingSpace = st.text_input("hasParkingSpace")
hasBalcony = st.text_input("hasBalcony")
hasElevator = st.text_input("hasElevator")
hasSecurity = st.text_input("hasSecurity")
hasStorageRoom = st.text_input("hasStorageRoom")

if st.button("Wyślij do modelu"):
    payload = {
        "city": city,
        "type": type_,
        "squareMeters": squareMeters,
        "rooms": rooms,
        "floor": floor,
        "floorCount": floorCount,
        "buildYear": buildYear,
        "latitude": latitude,
        "longitude": longitude,
        "centreDistance": centreDistance,
        "poiCount": poiCount,
        "schoolDistance": schoolDistance,
        "clinicDistance": clinicDistance,
        "postOfficeDistance": postOfficeDistance,
        "kindergartenDistance": kindergartenDistance,
        "restaurantDistance": restaurantDistance,
        "collegeDistance": collegeDistance,
        "pharmacyDistance": pharmacyDistance,
        "ownership": ownership,
        "buildingMaterial": buildingMaterial,
        "condition": condition,
        "hasParkingSpace": hasParkingSpace,
        "hasBalcony": hasBalcony,
        "hasElevator": hasElevator,
        "hasSecurity": hasSecurity,
        "hasStorageRoom": hasStorageRoom
    }

    try:
        r = requests.post("http://127.0.0.1:8000/predict", json=payload)
        if r.status_code == 200:
            st.success(f"Predykcja: {r.json()['prediction']}")
        else:
            st.error(f"Błąd API: {r.text}")
    except Exception as e:
        st.error(f"Błąd połączenia: {e}")
