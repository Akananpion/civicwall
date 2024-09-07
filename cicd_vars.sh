#!/usr/bin/env bash

# CI

set -u
: "${CI_REPOSITORY_URL}"

# ANSIBLE

set -u
: "${ANSIBLE_SERVER_HOST}"

set -u
: "${ANSIBLE_SERVER_USER}"

set -u
: "${ANSIBLE_DEPLOY_KEY}"

# DATABASE

set -u
: "${POSTGRES_DB}"

set -u
: "${POSTGRES_USER}"

set -u
: "${POSTGRES_PASSWORD}"

set -u
: "${POSTGRES_HOST}"

set -u
: "${POSTGRES_PORT}"

# EMAIL

set -u
: "${EMAIL_HOST}"

set -u
: "${EMAIL_PORT}"

set -u
: "${EMAIL_USE_TLS}"

set -u
: "${DEFAULT_FROM_EMAIL}"

set -u
: "${EMAIL_HOST_PASSWORD}"

# GENERAL

set -u
: "${DOMAIN_NAME}"
