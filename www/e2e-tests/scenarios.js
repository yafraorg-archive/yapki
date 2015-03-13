'use strict';

/* https://github.com/angular/protractor/blob/master/docs/toc.md */

describe('default redirect', function() {

  browser.get('index.html');

  it('should automatically redirect to /pki/db when location hash/fragment is empty', function() {
    expect(browser.getLocationAbsUrl()).toMatch("/pki/db");
  });


  describe('title of first page', function() {

    beforeEach(function() {
      browser.get('index.html#/pki/db');
    });


    it('should have a title', function() {
      expect(browser.getTitle()).toEqual('YAPKI Front End');
    });

  });

});
