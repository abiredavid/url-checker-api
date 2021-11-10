const PORT = process.env.PORT || 8000
const express = require("express")
const app = express()
const data = require("./data.json")


app.get('/', (req, res) => {
    res.json('The URL checker API Home')
})

app.get('/urlinfo/1/:url', (req, res) => {
    const url = req.params.url
    const hostname = url.replace(/:\d*/, "")
    result = data.filter( record => record.url === hostname)
    
    if (result.length === 0) {
        res.status(400).send('ERROR: hostname "' + hostname + '" does not exist in the database')
    }
    else {
        res.json(result[0])
    }   

})

app.listen(PORT, () => console.log(`server running on PORT ${PORT}`))

module.exports = app; // for testing