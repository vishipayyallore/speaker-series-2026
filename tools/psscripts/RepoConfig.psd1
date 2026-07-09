@{
  RepoName = 'speaker-series-2026'

  ExpectedFolders = @(
    'talks'
    'assets'
    'templates'
    'docs'
    'src'
    'tools'
    'tools\psscripts'
    'tools\pyscripts'
    '.github'
    '.cursor'
    '.cursor\rules'
    '.github\skills'
  )

  YamlCheckRoots = @(
    'docs'
    'talks'
  )

  # Speaker portfolio — no interview-prep language scan
  DisallowInterviewLanguage = $false
}
