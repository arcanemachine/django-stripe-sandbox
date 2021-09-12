describe("views: 'stripes:customer_update'", () => {
  const objectName = "Customer";
  const urlTest = `/${objectName.toLowerCase()}/1/update/`;

  it("Loads the page successfully", () => {

    cy.request(urlTest).then((response) => {
      expect(response.status).to.equal(200);
    })

    cy.visit(urlTest)
      .get('.body-title')
      .should('contain', `${objectName} Update`);
  });

  it("Updates the object", () => {
    // update the field(s)
    cy.visit(urlTest)
      .get('textarea[name="stripe_customer"]')
      .clear()
      .type('{"hello": "world"}', {parseSpecialCharSequences: false})
      .should('have.value', '{"hello": "world"}');

    // submit the form
    cy.get('form').submit()

    // page contains expected success message
    cy.get('.alert-success')
      .should('contain', `update success`);
  });

});
