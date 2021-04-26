var express = require('express');
var router = express.Router();

/* GET IP of connection.
  Should illustrate express behind proxy is working properly */
router.get('/', function(req, res, next) {
  res.send({'ip': req.ip, 'ips': req.ips});
});

module.exports = router;
