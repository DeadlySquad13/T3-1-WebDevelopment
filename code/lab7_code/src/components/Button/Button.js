export class Button {
  constructor(parent) {
    this.parent = parent;
  }

  getHTML() {
    return '<button class="Button" type="button">Clickity clackity!</button>';
  }

  render() {
    this.parent.insertAdjacentHTML(
      'beforeend', this.getHTML()
    );
  }
}
