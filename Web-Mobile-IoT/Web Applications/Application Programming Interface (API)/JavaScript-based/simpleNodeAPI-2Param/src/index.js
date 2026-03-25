/*
Simple Node application that take a request the print out the received parameters
@Author: DDNg
@Date: 2026/01/21
*/
const express = require('express')
const app = express()
const port = 5000

app.get('/', (req, res) => {
	//console.log(req)
	//console.log(req.query.param1)
	let part1 = "Hello, World!";
	let part2 = '<br>Params: {param1:'+ req.query.param1+', param2: '+req.query.param2+'}';
	let stringWithNewline = part1.concat('\n', part2);
	res.send(stringWithNewline)
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})