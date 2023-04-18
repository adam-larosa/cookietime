

const handleResponse = r => {
	if( r.ok ) {
		console.log( 'STATUS:', r.status )
		r.json().then( console.log )
	} else {
		console.error( 'STATUS:', r.status )
		r.text().then( console.warn )
	}
}

function App() {



	const testGetRequest = () => {
		fetch( '/users' ).then( handleResponse )
			.catch( e => console.error( 'GET users CATCH:', e ) )
	}



	const testPostRequest = () => {
		fetch( '/users', {
			method: 'POST', headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify( { 
				'lol': 'meow' 
			} )
		} ).then( handleResponse )
			.catch( e => console.error( 'POST users CATCH:', e ) )
	}



	return (
		<div className="App">

			<h1>hello world</h1>

			<button onClick={ testGetRequest }>
				GET request
			</button>

			<button onClick={ testPostRequest }>
				POST request
			</button>

		</div>
	);
}

export default App;
