const config = {
  branches: ['main', 'master'],

  "plugins": [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    [
      "@semantic-release/exec",
      {
        "prepareCmd": "echo ${nextRelease.version} > .VERSION ; poetry version $(cat .VERSION | sed 's/^[a-zA-Z]*//') ; poetry build"
      }
    ],
    [
      "@semantic-release/github",
      {
        "assets": [
          { "path": "dist/*" },
        ]
      }
    ],
    [
      "@semantic-release/changelog",
      {
        "changelogFile": "CHANGELOG.md"
      }
    ],
    [
      "@semantic-release/git",
      {
        "assets": ["CHANGELOG.md"],
        "message": "chore(Release 🚀): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}",
      }
    ]
  ],
};
module.exports = config;
