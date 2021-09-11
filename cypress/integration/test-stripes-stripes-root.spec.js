describe("views: 'stripes:stripes_root'", () => {
  const testUrl = Cypress.env('url_stripes_stripes_root');

  it("Loads the page successfully", () => {
    cy.request(testUrl).then((response) => {
      expect(response.status).to.equal(200);
    })
  });
});
