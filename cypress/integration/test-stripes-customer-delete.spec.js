describe.skip("views: 'stripes:customer_delete'", () => {
  const objectName = "Customer";
  const urlTest = `/${objectName.toLowerCase()}/2/delete/`;

  it("Loads the page successfully", () => {
    cy.request(urlTest).then((response) => {
      expect(response.status).to.equal(200);
    })

    cy.visit(urlTest)
      .get('.body-title')
      .should('contain', `${objectName} Delete`);
  });

  it("Deletes the object", () => {
    // submit the form
    cy.visit(urlTest)
      .get('form').submit()

    // page contains expected success message
    cy.get('.alert-success')
      .should('contain', `delete success`);
  });

});

describe("views: 'stripes:customer_delete_newest'", () => {
  const objectName = "Customer";
  const urlTest = `/${objectName.toLowerCase()}/newest/delete/`;

  it("Loads the page successfully", () => {
    cy.request(urlTest).then((response) => {
      expect(response.status).to.equal(200);
    })

    cy.visit(urlTest)
      .get('.body-title')
      .should('contain', `${objectName} Delete`);
  });

  it("Deletes the object", () => {
    // submit the form
    cy.visit(urlTest)
      .get('form').submit()

    // page contains expected success message
    cy.get('.alert-success')
      .should('contain', `delete success`);
  });

});
