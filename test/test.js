process.env.NODE_ENV = 'test';

let chai = require('chai');
let chaiHttp = require('chai-http');
let server = require('../index');
let should = chai.should();

chai.use(chaiHttp);

describe('/GET /', () => {
  it('it should GET api home', (done) => {
    chai.request(server)
        .get('/')
        .end((err, res) => {
              res.should.have.status(200);
              res.body.should.be.a('string');
          done();
        });
  });
  describe('/GET /urlinfo/1/:urlQueryString', () => {
    it('it should return safe for worksgreat.it:8080/?dependencies?sortBy=dependency&order=asc&page=1&perPage=500', (done) => {
      chai.request(server)
          .get('/urlinfo/1/worksgreat.it:8080/?dependencies?sortBy=dependency&order=asc&page=1&perPage=500')
          .end((err, res) => {
              res.should.have.status(200);
              res.body.should.be.a('object');
              res.body.should.have.property('url').eql('worksgreat.it');
              res.body.should.have.property('isSafe').eql(true);
            done();
          });
      });
  });
  
  describe('/GET /urlinfo/1/:urlQueryString', () => {
    it('it should return unsafe for terrible.com:80/?dependencies?sortBy=dependency&order=asc&page=3&perPage=500', (done) => {
      chai.request(server)
          .get('/urlinfo/1/terrible.com:80/?dependencies?sortBy=dependency&order=asc&page=3&perPage=500')
          .end((err, res) => {
              res.should.have.status(200);
              res.body.should.be.a('object');
              res.body.should.have.property('url').eql('terrible.com');
              res.body.should.have.property('isSafe').eql(false);
            done();
          });
    });
  });

  describe('/GET /urlinfo/1/:urlQueryString', () => {
    it('it should return unsafe for unrestricted.com:8080/?dependencies?sortBy=dependency&order=asc&page=1&perPage=500', (done) => {
      chai.request(server)
          .get('/urlinfo/1/unrestricted.com:8080/?dependencies?sortBy=dependency&order=asc&page=1&perPage=500')
          .end((err, res) => {
              res.should.have.status(200);
              res.body.should.be.a('object');
              res.body.should.have.property('url').eql('unrestricted.com');
              res.body.should.have.property('isSafe').eql(false);
            done();
          });
    });
  });

  describe('/GET /urlinfo/1/:urlQueryString', () => {
    it('it should return 400 for unrestricted.gov:8000/?dependencies?sortBy=dependency&order=asc&page=1&perPage=500', (done) => {
      chai.request(server)
          .get('/urlinfo/1/unrestricted.gov:8000/?dependencies?sortBy=dependency&order=asc&page=1&perPage=500')
          .end((err, res) => {
              res.should.have.status(400);
              res.body.should.be.a('object');
            done();
          });
      });
    });
});


