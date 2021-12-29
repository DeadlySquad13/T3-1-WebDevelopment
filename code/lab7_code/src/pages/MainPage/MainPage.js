import { Button } from '../../components/Button/Button.js';
import { AnimeCard } from '../../components/AnimeCard/AnimeCard.js';

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

  render() {
    const button = new Button(this.parent);
    const anime = {
      title: 'Test',
      description: 'lalala'
    }
    const animeCard = new AnimeCard(this.parent, button, anime);
    const children = [animeCard]

    const html = this.getHTML(children);

    this.parent.insertAdjacentHTML('beforeend', html);
  }
}
