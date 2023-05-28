Feature: tester la fonctionnalité de la page d acceuil Ebay
  entantque utlisteur je log dans l application Ebaby et valider les
  recherches effectuer sur cette application
  ecrit par krimou le 14/03/2023

  """Background: les étapes communes
     Given je suis sur la page d accuil d Ebay"""


  Scenario : A lien de recherche avances
    Given je suis sur la page d accuil d Ebay
    When je cliquer sur lien avance
    Then je navigue vers la page recherche avancé

  Scenario: B nombre d’éléments de recherche
    Given je suis sur la page d accuil d Ebay
    When Je recherche 'iPhone 11'
    Then Je valide au moins 1000 éléments de recherche présents

  Scenario: C nombre d’éléments recherchés2
    Given je suis sur la page d accuil d Ebay
    When Je recherche 'Toy Cars'
    Then Je valide au moins 100 éléments de recherche présents

  Scenario: :D Rechercher un article dans la catégorie
    Given je suis sur la page d accuil d Ebay
    When Je recherche 'soap' dans la catégorie 'BaBy'
    Then Je valide au moins 50 éléments de recherche présents
