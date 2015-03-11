'use strict';

/* https://github.com/angular/protractor/blob/master/docs/toc.md */

describe('my app', function() {

  browser.get('index.html');

  it('should automatically redirect to /view1 when location hash/fragment is empty', function() {
    expect(browser.getLocationAbsUrl()).toMatch("/pki/db");
  });


  describe('view1', function() {

    beforeEach(function() {
      browser.get('index.html#/pki/db');
    });


    it('should render openssl db view when user navigates to /pki/db', function() {
      expect(element.all(by.css('[ui-view] p')).first().getText()).
        toMatch(/partial for view 1/);
    });

  });

});
