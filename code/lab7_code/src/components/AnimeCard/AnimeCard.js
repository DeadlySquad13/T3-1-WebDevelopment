export class AnimeCard {
  props = {
    title: null,
    description: null,
    poster: null
  }

  constructor(parent, children, props) {
    this.parent = parent;
    this.children = children;
    this.props = props;
  }

  getHTML() {
    const { title, poster, description } = this.props;
    return (`
      <div class="AnimeCard">
        <h2>${title}</h2>
        <img src="${poster}" alt="${title}"/>
        <p>${description}</p>
        <footer class="AnimeCard__Footer">
          ${this.children.reduce((html, child) => (
                html + child.getHTML()
            ), '')
          }
        </footer>
      </div>
      `)
  }

  render() {
    const html = this.getHTML();
    this.parent.insertAdjacentHTML('beforeend', html);
  }
}
