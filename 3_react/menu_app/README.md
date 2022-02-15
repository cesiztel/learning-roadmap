## Bit of history

React was first created by Jordan Walke, a software engineer at Facebook. It was incorporated into Facebook’s newsfeed in 2011 and later on Instagram when it was acquired by Facebook in 2012. At JSConf 2013, React was made open source, and it joined the crowded category of UI libraries like jQuery, Angular, Dojo, Meteor, and others. At that time, React was described as “the V in MVC.”

React was billed as a library: concerned with implementing a specific set of features, not providing a tool for every use case.

```
React.createElement(type, props, [arguments])
```

Any element that has an HTML class attribute is using className for that property instead of class. Since class is a reserved word in JavaScript, we have to use className to define the class attribute of an HTML element.

When we build a list of child elements by iterating through an array, React likes each of those elements to have a key property. The key property is used by React to help it update the DOM efficiently.

```
const bakedSalmonIngredients = React.createElement(
  "ul",
  { className: "ingredients " },
  items.map((ingredient, i) =>
    React.createElement("li", { key: i }, ingredient)
  )
);
```

## JSX

```
React Element     React.createElement(IngredientsList, { list: [...] });
                                            |              |
     JSX                             <IngredientsList list={[...]}/>
```

## React Fragments

```
function Cat({ name }) {
  return (
    <> // fragment to surround the siblings
      <h1>The cat's name is {name}</h1>
      <p>He's good.</h1>
    </>
  )
}

ReactDOM.render(
  <Cat name="Jungle" />,
  document.getElementById("root")
);
```

## Webpack

Webpack is billed as a module bundler. A module bundler takes all of our different files (Javascript, LESS, CSS, JSX, ESNext and so on) and turns them into a single file. The two main benefits of bundling are `modularity` and `network performance`.

Modularity will allow you to break down your source code into parts, or modules, that are easier to work with, especially in a team environment.

Network performance is gained by only needing to load one dependency in the browser: the bundle. Each `script` tag makes an HTTP request, and there's latency penalty for each HTTP request. Bundling all the dependecies into a single file allows you to load everything with one HTTP request, thereby avoiding additional latency

Also can handle:

- Code splitting
- Minification
- Feature Flagging
- Hot Module Replacement (HMR)

## 📝 Your Notes

Normally an interactive application will need to hold state somewhere. In React,
you use special functions called "hooks" to do this. Common built-in hooks
include:

- `React.useState`
- `React.useEffect`
- `React.useContext`
- `React.useRef`
- `React.useReducer`

Each of the hooks has a unique API. You can call them inside your custom React component function to store data
or perform actions.

`React.useEffect` is a built-in hook that allows you to run some custom code after React renders (and re-renders)
your component to the DOM. It accepts a callback function which React will call after the DOM has been updated:

```javascript
React.useEffect(() => {
  // your side-effect code here.
  // .. you can make an update based on HTTP request or interact with
  // browser API
});
```

# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
