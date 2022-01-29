import { render, screen, fireEvent } from '@testing-library/react';
import Counter from '../../01_Counter/Counter';

test('starting the counter on 0 after clicker the counter value is 1', () => {
    render(<Counter />)

    fireEvent.click(screen.getByRole('button'));

    expect(screen.getByRole('button').textContent).toBe("1");
});

test('starting the counter on 0 after press 5 times the counter value is 5', () => {
    render(<Counter />)
    const counterButton = screen.getByRole('button');

    for (let click = 0; click < 5; click++) {
        fireEvent.click(counterButton);
    }

    expect(screen.getByRole('button').textContent).toBe("5");
});