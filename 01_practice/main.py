INFO = {
    "Iron Man": {
        "realName": "Tony Stark",
        "powers": ["superGenius", "superArmour"],
        "team": "Avengers"
    },
    "Captain America": {
        "realName": "Steve Rogers",
        "powers": ["superStrength", "superShield"],
        "team": "Avengers"
    },
    "Black Widow": {
        "realName": "Natasha Romanoff",
        "powers": ["superSpy"],
        "team": "Avengers"
    },
    "Thor": {
        "realName": "Thor Odinson",
        "powers": ["superStrength", "superWeather"],
        "team": "Avengers"
    },
    "Hulk": {
        "realName": "Bruce Banner",
        "powers": ["superStrength", "superAngry"],
        "team": "Avengers"
    },
    "Spiderman": {
        "realName": "Peter Parker",
        "powers": ["superStrength", "superAgility"],
        "team": "Avengers"
    },
}

def showInfoSuperHero(superHero):
    return {
        "superHero": superHero,
        "realName": INFO[superHero]["realName"],
        "powers": INFO[superHero]["powers"],
        "team": INFO[superHero]["team"]
    }
