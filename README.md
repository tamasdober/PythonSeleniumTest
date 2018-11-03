
SUMMARY
=========

This is an extract from the initial Python-based test framework with the goal of replacing an earlier Java-based framework.
The initial version served as a Proof Of Concept, which was compared with a Ruby-based approach - and was chosen to develop further.

This Python test framework got later Dockerized, based on Ubuntu. 
The Dockerfile (not included here) was to create an image for use on Jenkins for Selenium testing with Chrome and Python 3.6.
It incorporated Xfce and VNC (port 5901) and NoVNC (port 6901) so the actual tests could be followed either in a browser-window or through VNC Viewer.

APPLYING PAGE OBJECT MODEL
============================

The aim of this test project is to verify some UI and also some REST interfaces of the project.

The implementation drives to provide a Page Object Model structure.
For this, a base page is being provided for both types (UI & REST) of tests, to inherit general functions from.

The project consists of three main packages: pom, tests and utilities.
The first one further divided into locators and pages, by areas of functionality - thus the CSS, Xpath etc. selector data got separated in order to provide clean code about the actual pages.
The third package, utilities is to provide methods to get Hash-based message authentication code (HMAC) by accessing some debug pages.

ABOUT THE TESTS
================

The third package is about the actual tests. 
Every test class has some setup with some ChromeOptions, which has been necessary when running the tests from the Docker container (for the VNC functionality).
Also here we do the login, using values, passed in as environment variables.
The tests try to provide context via comments and docstrings.
A useful solution to verify that all expected UI elements do exists is to have parameterized testing (see VenueListTests).
There is also an attempt to provide a wait functionality for Ajax calls on some jQuery pages.
