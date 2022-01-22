import styled from 'styled-components';

export const Li = styled.li<{ color?: string; hoverColor?: string; }>`
  list-style-type: none;

  a {
    text-decoration: none;
    color: ${({ color }) => color || 'white'};
  }

  a:hover {
    color: ${({ hoverColor }) => hoverColor || '#d1f1f4'};
  }

  font-size: 24px;
`

