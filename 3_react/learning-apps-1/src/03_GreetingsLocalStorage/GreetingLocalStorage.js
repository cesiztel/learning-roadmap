import React from 'react'

function GreetingLocalStorage({initialName = ''}) {
    initialName = window.localStorage.getItem('name') || initialName
    const [name, setName] = React.useState(initialName)

    React.useEffect(() => {
        window.localStorage.setItem('name', name)
    });

    function handleOnChange(event) {
        setName(event.target.value)
    }

    return(
        <div>
            <form>
                <label htmlFor="name">Name: </label>
                <input
                    value={name}
                    onChange={handleOnChange}
                    type="text"
                    id="name"
                    aria-label="name-input"
                />
                <p>
                    { name ? <strong>Hello {name}!</strong> : 'Please type your name' }
                </p>
            </form>
        </div>
    );
}

export default GreetingLocalStorage