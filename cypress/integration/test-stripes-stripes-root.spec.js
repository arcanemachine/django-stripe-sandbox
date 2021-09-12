describe("views: 'stripes:stripes_root'", () => {
  const urlTest = Cypress.env('url_stripes_stripes_root');

  it("Loads the page successfully", () => {
    cy.request(urlTest).then((response) => {
      expect(response.status).to.equal(200);
    })
  });
});
