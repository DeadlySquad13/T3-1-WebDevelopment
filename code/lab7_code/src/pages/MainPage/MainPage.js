import { Button } from '../../components/Button/Button.js';
import { AnimeCard } from '../../components/AnimeCard/AnimeCard.js';
import { ajax } from '../../modules/ajax.js';
import { urls } from '../../modules/urls.js';
import { fetchData } from '../../modules/fetchData.js';

export class MainPage {
  constructor(parent) {
    this.parent = parent;
  }

  getHTML(children) {
    return (`
      <div class="MainPage">
        ${children.reduce((html, child) => (
              html + child.getHTML()
          
          ), '')
        }
      </div>
      `)
  }

  async render() {
    const button = new Button(this.parent);

    const data = await fetchData(urls.anime(3));


    //const anime = {
      //title: 'Test',
      //description: 'lalala'
    //}
    const animeCard = new AnimeCard(this.parent, button, data);
    const children = [animeCard]

    const html = this.getHTML(children);

    this.parent.insertAdjacentHTML('beforeend', html);
  }
}
