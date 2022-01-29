import React from 'react'

function Greeting() {
    const [name, setName] = React.useState("");

    function handleOnChange(event) {
        setName(event.target.value)
    }

    return(
        <div>
            <form>
                <label htmlFor="name">Name: </label>
                <input onChange={handleOnChange} type="text" id="name" aria-label="name-input" />
                <p>
                    { name ? <strong>Hello {name}!</strong> : 'Please type your name' }
                </p>
            </form>
        </div>
    );
}

export default Greeting