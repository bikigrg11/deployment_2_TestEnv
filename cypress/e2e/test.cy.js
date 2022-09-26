describe('Heading', () => {
    it('has the right title', () => {
        cy.visit('http://3.87.190.123:5000/')

        cy.get('title')
            .invoke('text')
            .should("equal", "URL Shortener")
    });

});
