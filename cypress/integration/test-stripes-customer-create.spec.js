describe("views: 'stripes:customer_create'", () => {
  const urlTest = Cypress.env('url_stripes_customer_create');

  it("Loads the page successfully", () => {
    cy.request(urlTest).then((response) => {
      expect(response.status).to.equal(200);
    })
  });

  it("Creates a new Customer using the form", () => {
    // get object count before creating new object
    let oldCustomerCount, newCustomerCount;
    cy.visit(Cypress.env('url_stripes_customer_list'))
      .get('[data-cy="object-list"]')
      .then((ul) => {
        oldCustomerCount = ul.children().length;
        console.log(`oldCustomerCount: ${oldCustomerCount}`);
      });

    // get id of last object before continuing
    let highestValueId;
    cy.get('[data-cy="object-list-item"]').last().invoke('attr', 'data-cy-id')
      .then((id) => {
        highestValueId = Number(id);
        console.log(`highestValueId: ${highestValueId}`);
      });

    // create customer
    cy.visit(urlTest)
      .get('[data-cy="base-form-button-submit"]')
      .click()

    // user is redirected to expected page
    cy.location().should((loc) => {
      expect(loc.pathname).to.eq(Cypress.env('url_stripes_customer_list'))
    });
    
    // object count has increased by one
    cy.get('[data-cy="object-list"]')
      .then((ul) => {
        newCustomerCount = ul.children().length;
        console.log(`newCustomerCount: ${newCustomerCount}`);
        cy.expect(newCustomerCount).to.eq(oldCustomerCount + 1);
      });

    // page contains expected success message
    cy.get('.alert-success')
      .should('contain', `create success`);

  });
});
