const PORT = process.env.PORT || 8000
const express = require("express")
const app = express()
const data = require("./data.json")


app.get('/urlinfo/1/:url', (req, res) => {
    const url = req.params.url
    const hostname = url.replace(/:\d*/, "")
    result = data.filter( record => record.url === hostname)
    
    res.json(result[0])

})

app.listen(PORT, () => console.log(`server running on PORT ${PORT}`))