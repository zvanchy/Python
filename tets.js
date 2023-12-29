const captialCities = [
    {
        sr: 1,
        zone: "Bagmati",
        capital: "Kathmandu"

    },
    {
        sr: 2,
        zone: "Koshi",
        capital: "Biratnagar"

    },
    {
        sr: 3,
        zone: "Sagarmatha",
        capital: "Saptari"

    },
    {
        sr: 4,
        zone: "Janakpur",
        capital: "Janakpur"

    },
]


captialCities.sort((a, b) => a.capital < b.capital ? 1 : -1);
