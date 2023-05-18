const searchForm = document.getElementById('search-form')
const searchInput = document.getElementById('search-input')
const resultsBox = document.getElementById('results-box')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
// console.log(csrf)

searchInput.addEventListener('keyup', e=> {
    console.log(e.target.value)
})