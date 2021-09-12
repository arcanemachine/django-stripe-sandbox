describe("views: 'stripes:customer_detail'", () => {
  it("Loads the page successfully", () => {
    const objectName = "Customer";
    const urlTest = `/${objectName.toLowerCase()}/1/`;

    cy.request(urlTest).then((response) => {
      expect(response.status).to.equal(200);
    })

    cy.visit(urlTest)
      .get('.body-title')
      .should('contain', `${objectName} Detail`);
  });

});
