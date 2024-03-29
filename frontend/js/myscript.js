const getBooks = async () => {
    const response = await fetch('http://localhost:5000/books/5')
    const result = await response.json()

    console.log(result)
}