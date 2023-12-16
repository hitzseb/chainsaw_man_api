# Chainsaw Man API

The Chainsaw Man API provides comprehensive information about the world of Chainsaw Man, including characters, sagas, arcs, manga volumes, anime episodes, species, and more. The API is built using Django and utilizes JWT (JSON Web Token) for enhanced access.

## Usage

### Authentication
While basic access is available for anonymous users, enhanced features and higher request limits can be unlocked by registering and obtaining a JWT token. To authenticate, include the access token in the Authorization header of your requests. Token refresh is available at `/api/token/refresh/`.

**Note:** Keep tokens secure and avoid sharing them publicly.

### Example Request

```
curl https://chainsawmanapi.pythonanywhere.com/api/character/Pochita/
```

```
{
    "name": "Pochita",
    "picture": "https://chainsawmanapi.pythonanywhere.com/api/character/picture/Pochita.webp/",
    "description": "Pochita (ポチタ?) is the Chainsaw Devil (チェンソーの悪あく魔ま Chensō no Akuma?) who embodies the fear of chainsaws. He was the original Chainsaw Man (チェンソーマン Chensō Man?) prior to becoming Denji's heart. He is the overarching titular protagonist of the series.",
    "status": "Alive",
    "species": {
        "name": "Hybrid"
    },
    "manga_debut": {
        "number": 1,
        "title": "Dog & Chainsaw",
        "cover": "https://chainsawmanapi.pythonanywhere.com/api/manga/cover/Chapter_1.webp",
        "url": "https://chainsawmanapi.pythonanywhere.com/api/manga/1/"
    },
    "anime_debut": {
        "number": 1,
        "title": "Dog & Chainsaw",
        "still": "https://chainsawmanapi.pythonanywhere.com/api/anime/still/Episode_1.webp/",
        "date": "2022-10-11",
        "url": "https://chainsawmanapi.pythonanywhere.com/api/anime/1/"
    }
}
```


## Endpoints

- **Sagas:**
  - List all sagas: `/api/saga/`
  - Detailed information about a specific saga: `/api/saga/number/`

- **Arcs:**
  - List all arcs: `/api/arc/`
  - Detailed information about a specific arc: `/api/arc/number/`

- **Volumes:**
  - List all manga volumes: `/api/volume/`
  - Detailed information about a specific volume: `/api/volume/number/`

- **Manga Chapters:**
  - List all manga chapters: `/api/manga/`
  - Detailed information about a specific manga chapter: `/api/manga/number/`

- **Anime Seasons:**
  - List all anime seasons: `/api/season/`
  - Detailed information about a specific anime season: `/api/season/number/`

- **Anime Episodes:**
  - List all anime episodes: `/api/anime/`
  - Detailed information about a specific anime episode: `/api/anime/number/`

- **Species:**
  - List all species: `/api/species/`
  - Detailed information about a specific species by name: `/api/species/name/`

- **Characters:**
  - List all characters: `/api/character/`
  - Detailed information about a specific character by name: `/api/character/name/`



## Technologies Used

- Python 3.10
- Django 4.2.7
- Django Rest Framework 3.14.0
- djangorestframework-simplejwt 5.3.0
- drf-yasg 1.21.7
- Bootstrap 5.3
- Other packages and dependencies as specified in `requirements.txt`



## About

This project is developed and maintained by Sebastian Hitz. It is open source under the MIT license. The data is sourced from the Chainsaw Man Wiki.

**GitHub Repository:** [Chainsaw Man API](https://github.com/your-username/chainsaw-man-api)

Feel free to contribute and improve the Chainsaw Man API!
