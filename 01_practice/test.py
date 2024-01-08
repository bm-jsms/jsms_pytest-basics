from main import showInfoSuperHero

def test_one_showInfoSuperHero():
    assert showInfoSuperHero("Iron Man") == {
        "superHero": "Iron Man",
        "realName": "Tony Stark",
        "powers": ["superGenius", "superArmour"],
        "team": "Avengers"
    }

def test_two_showInfoSuperHero():
    assert showInfoSuperHero("Captain America") == {
        "superHero": "Captain America",
        "realName": "Steve Rogers",
        "powers": ["superStrength", "superShield"],
        "team": "Avengers"
    }

def test_three_showInfoSuperHero():
    assert showInfoSuperHero("Black Widow") == {
        "superHero": "Black Widow",
        "realName": "Natasha Romanoff",
        "powers": ["superSpy"],
        "team": "Avengers"
    }

def test_four_showInfoSuperHero():
    assert showInfoSuperHero("Thor") == {
        "superHero": "Thor",
        "realName": "Thor Odinson",
        "powers": ["superStrength", "superWeather"],
        "team": "Avengers"
    }

def test_five_showInfoSuperHero():
    assert showInfoSuperHero("Hulk") == {
        "superHero": "Hulk",
        "realName": "Bruce Banner",
        "powers": ["superStrength", "superAngry"],
        "team": "Avengers"
    }

def test_six_showInfoSuperHero():
    assert showInfoSuperHero("Spiderman") == {
        "superHero": "Spiderman",
        "realName": "Peter Parker",
        "powers": ["superStrength", "superAgility"],
        "team": "Avengers"
    }
