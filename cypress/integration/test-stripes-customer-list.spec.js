describe("views: 'stripes:customer_list'", () => {
  const urlTest = Cypress.env('url_stripes_customer_list');

  it("Loads the page successfully", () => {
    cy.request(urlTest).then((response) => {
      expect(response.status).to.equal(200);
    })
  });
});
