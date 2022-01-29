import React from 'react';
import './Counter.css';

function Counter() {
    const [count, setCount] = React.useState(0)
    const increment = () => setCount(count + 1)

    return <button className="Counter" onClick={increment}>{count}</button>
}

export default Counter;