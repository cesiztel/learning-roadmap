import { render, screen, fireEvent } from '@testing-library/react';
import Greeting from "../../02_Greeting/Greeting";

test('After render initial test: Please type your name', () => {
   const expectedText = 'Please type your name';
   const { container } = render(<Greeting />)

   expect(container.querySelector('p').innerHTML).toBe(expectedText)
});

test('When type a name, the text is: Hello {name}!', () => {
    const name = 'Mark';
    const expectedText = `Hello ${name}!`
    const { container } = render(<Greeting />)
    const input = screen.getByLabelText('name-input')

    fireEvent.change(input, { target: { value: name }})

    expect(input.value).toBe(name)
    expect(container.querySelector('p > strong').innerHTML).toBe(expectedText)
})