class Urls {
  constructor() {
    this.url = 'http://localhost:8000/';
  }

  animes() {
    return `${this.url}anime/`;
  }

  anime(id) {
    return `${this.url}anime/${id}/`;
  }
}

export const urls = new Urls();

