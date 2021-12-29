import { Button } from '../../components/Button/Button.js';
import { AnimeCard } from '../../components/AnimeCard/AnimeCard.js';
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
    const currentAnimeId = 3;

    const buttonPrevious = new Button(this.parent, {
      text: 'Previous',
      onClick: () => {
        console.log('test', currentAnimeId);
      }
    });
    const buttonNext = new Button(this.parent, {
      text: 'Next',
      onClick: function() { console.log('test', currentAnimeId); }
    });

    const data = await fetchData(urls.anime(currentAnimeId));
    const animeCard = new AnimeCard(this.parent, [buttonPrevious, buttonNext], data);

    const children = [animeCard]
    const html = this.getHTML(children);

    this.parent.insertAdjacentHTML('beforeend', html);
  }
}
